# File: routers/perhitungan.py (Final)

import numpy as np
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# PERBAIKAN: Impor List dan Dict dari modul typing
from typing import List, Dict
import crud, schemas, models
from database import get_db
from routers.users import get_current_active_user

router = APIRouter(prefix="/perhitungan", tags=["Perhitungan ARAS"])

def calculate_rank_sum_weights(peringkat_kriteria: List[str]) -> Dict[str, float]:
    n = len(peringkat_kriteria)
    bobot = {}
    total_bobot = n * (n + 1) / 2
    for i, kode_kriteria in enumerate(peringkat_kriteria):
        rank = i + 1
        weight = (n - rank + 1) / total_bobot
        bobot[kode_kriteria] = weight
    return bobot

@router.post("/", response_model=schemas.HasilPerhitungan)
def do_aras_calculation(
    data_peringkat: schemas.BobotKriteria,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    alternatifs = crud.get_all_alternatif(db)
    kriterias = crud.get_all_kriteria(db)
    penilaians = db.query(models.Penilaian).all()

    if not alternatifs or not kriterias:
        raise HTTPException(status_code=404, detail="Data alternatif atau kriteria tidak ditemukan")

    bobot_ternormalisasi = calculate_rank_sum_weights(data_peringkat.peringkat)
    kriterias.sort(key=lambda x: x.id_kriteria)
    penilaian_map = {p.id_alternatif: p for p in penilaians}

    matrix_x = np.zeros((len(alternatifs), len(kriterias)))
    for i, alt in enumerate(alternatifs):
        penilaian_alt = penilaian_map.get(alt.id_alternatif)
        if not penilaian_alt: continue
        matrix_x[i, 0] = penilaian_alt.jarak_km
        matrix_x[i, 1] = penilaian_alt.peluang_karir
        matrix_x[i, 2] = penilaian_alt.reputasi_perusahaan
        matrix_x[i, 3] = penilaian_alt.relevansi_proyek
        matrix_x[i, 4] = penilaian_alt.teknologi_baru
        matrix_x[i, 5] = penilaian_alt.kualitas_mentorship

    x0 = np.zeros(len(kriterias))
    for j, k in enumerate(kriterias):
        if k.tipe_kriteria == models.TipeKriteriaEnum.benefit:
            x0[j] = np.max(matrix_x[:, j])
        else:
            x0[j] = np.min(matrix_x[:, j])

    extended_matrix = np.vstack([x0, matrix_x])
    norm_matrix = np.zeros_like(extended_matrix, dtype=float)
    sum_cols = np.zeros(len(kriterias))
    for j, k in enumerate(kriterias):
        col_data = extended_matrix[:, j]
        if k.tipe_kriteria == models.TipeKriteriaEnum.benefit:
            sum_cols[j] = np.sum(col_data)
        else:
            if np.any(col_data == 0):
                raise HTTPException(status_code=400, detail=f"Kriteria {k.kode_kriteria} memiliki nilai 0.")
            sum_cols[j] = np.sum(1 / col_data)

    for i in range(extended_matrix.shape[0]):
        for j, k in enumerate(kriterias):
            if sum_cols[j] == 0: continue
            if k.tipe_kriteria == models.TipeKriteriaEnum.benefit:
                norm_matrix[i, j] = extended_matrix[i, j] / sum_cols[j]
            else:
                norm_matrix[i, j] = (1 / extended_matrix[i, j]) / sum_cols[j]

    bobot_array = np.array([bobot_ternormalisasi[k.kode_kriteria] for k in kriterias])
    weighted_matrix = norm_matrix * bobot_array
    s_values = np.sum(weighted_matrix, axis=1)
    s0_optimal = s_values[0]

    if s0_optimal == 0:
        raise HTTPException(status_code=500, detail="Perhitungan gagal, nilai S0 adalah nol.")

    k_values = s_values[1:] / s0_optimal
    hasil_list = [{"id_alternatif": alt.id_alternatif, "nama_perusahaan": alt.nama_perusahaan, "skor_utilitas": k_values[i]} for i, alt in enumerate(alternatifs)]
    hasil_list.sort(key=lambda x: x["skor_utilitas"], reverse=True)
    ranked_results = [{"peringkat": i + 1, **res} for i, res in enumerate(hasil_list)]

    riwayat = crud.create_riwayat(db, user_id=current_user.id_user, bobot={"peringkat_user": data_peringkat.peringkat}, hasil=ranked_results)

    return {"id_riwayat": riwayat.id_riwayat, "tanggal_perhitungan": riwayat.tanggal_perhitungan, "hasil": ranked_results}
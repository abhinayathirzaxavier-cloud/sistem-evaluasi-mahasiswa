
print("=== SISTEM EVALUASI MAHASISWA ===")

# 1. Input nilai dan kehadiran
tugas = float(input("Masukkan nilai Tugas (0-100): "))
uts = float(input("Masukkan nilai UTS (0-100): "))
uas = float(input("Masukkan nilai UAS (0-100): "))
kehadiran = float(input("Masukkan persentase kehadiran (0-100): "))


nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

print(f"\nNilai Akhir: {nilai_akhir:.2f}")

lulus = (nilai_akhir >= 75) and (kehadiran >= 80)

predikat = (
    (nilai_akhir >= 85)
    and (kehadiran >= 90)
    and (nilai_akhir % 2 == 0)
)

if not lulus:
    print("Status: BELUM LULUS")
elif predikat:
    print("Status: LULUS DENGAN PREDIKAT")
else:
    print("Status: LULUS")

print("\n=== RINCIAN PENILAIAN ===")
print(f"Nilai Tugas       : {tugas}")
print(f"Nilai UTS         : {uts}")
print(f"Nilai UAS         : {uas}")
print(f"Kehadiran         : {kehadiran}%")
print(f"Nilai akhir >= 75 : {nilai_akhir >= 75}")
print(f"Kehadiran >= 80%  : {kehadiran >= 80}")
print(f"Nilai akhir >= 85 : {nilai_akhir >= 85}")
print(f"Kehadiran >= 90%  : {kehadiran >= 90}")
print(f"Nilai akhir genap : {nilai_akhir % 2 == 0}")

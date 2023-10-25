def convert_ke_menit(minggu):
    def hari(hari):
        def jam(jam):
            def menit(menit):
                return (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
            return menit
        return jam
    return hari

data = ["3 minggu 3 hari 7 jam 21 menit", 
        "5 minggu 5 hari 8 jam 11 menit", 
        "7 minggu 1 hari 5 jam 33 menit"]

convert = convert_ke_menit

OutputData = []
for entry in data:
    data_split = entry.split()
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int(data_split[6])

    result = convert(minggu)(hari)(jam)(menit)
    OutputData.append(result)

print(OutputData)

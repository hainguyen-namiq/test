import os



# text = ""
# nameward = {
# "brand": "Ford"
# }
# ward = ["tan binh",
#         "nha be",
#         "hoc mon",
#         "cu chi",
#         "can gio",
#         "binh chanh",
#         "binh tan",
#         "go vap",
#         "binh thanh",
#         "phu nhuan",
#         "tan phu",
#         "thu duc",
#
#         ]
thisdict = {
  "tan binh": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15",
  "nha be": "Hiệp Phước, Long Thới, Nhơn Đức, Phú Xuân , Phước Kiển, Phước Lộc, Nhà Bè ",
  "hoc mon": "Bà Điểm, Đông Thạnh, Nhị Bình, Tân Hiệp, Tân Thới Nhì, Tân Xuân, Thới Tam Thôn, Trung Chánh, Xuân Thới Đông, Xuân Thới Sơn, Xuân Thới Thượng",
  "cu chi": "Củ Chi, An Nhơn Tây, An Phú, Bình Mỹ, Hòa Phú, Nhuận Đức, Phạm Văn Cội, Phú Hòa Đông, Phú Mỹ Hưng, Phước Hiệp, Phước Thạnh, Phước Vĩnh An, Tân An Hội, Tân Phú Trung, Tân Thạnh Đông, Tân Thạnh Tây, Tân Thông Hội, Thái Mỹ, Trung An, Trung Lập Hạ, Trung Lập Thượng",
  "can gio": "Cần Thạnh, An Thới Đông, Bình Khánh, Long Hòa, Lý Nhơn, Tam Thôn Hiệp, Thạnh An",
  "binh chanh": "Tân Túc, An Phú Tây, Bình Chánh, Bình Hưng, Bình Lợi, Đa Phước, Hưng Long, Lê Minh Xuân, Phạm Văn Hai, Phong Phú, Quy Đức, Tân Kiên, Tân Nhựt, Tân Quý Tây, Vĩnh Lộc A, Vĩnh Lộc B",
  "binh tan": "An Lạc, An Lạc A, Bình Hưng Hòa, Bình Hưng Hòa A, Bình Hưng Hòa B, Bình Trị Đông, Bình Trị Đông A, Bình Trị Đông B, Tân Tạo, Tân Tạo A",
  "go vap": "1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17",
  "binh thanh": "1, 2, 3, 5, 6, 7, 11, 12, 13, 14, 15, 17, 19, 21, 22, 24, 25, 26, 27, 28",
  "phu nhuan": "1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17",
  "tan phu": "Hiệp Tân, Hòa Thạnh, Phú Thạnh, Phú Thọ Hòa, Phú Trung, Sơn Kỳ, Tân Quý, Tân Sơn Nhì, Tân Thành, Tân Thới Hòa, Tây Thạnh",
  "thu duc": "Bình Chiểu, Bình Thọ, Hiệp Bình Chánh, Hiệp Bình Phước, Linh Chiểu, Linh Ðông, Linh Tây, Linh Trung, Linh Xuân, Tam Bình, Tam Phú, Trường Thọ"
}
parent_dir = "/home/nhh/dev/test"

for idx in thisdict:

    path = os.path.join(parent_dir, idx)
    path_ward = os.path.join(path, "ward.txt")
    f1 = open(path_ward, "w")

    list = thisdict[idx].split(', ')
    for id in list:
        f1.write(id + "\n")

    f1.close()
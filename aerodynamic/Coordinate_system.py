class CORD2R

    def __init__(self):

        # A , B and C are the coordinates of  3 points (reference) defined in this coordinate system
        self.cid = 0  # coordinate id
        self.rid = 0  # Identification of a coord system defined independently from this coord system
        self.A1 = 0.0
        self.A2 = 0.0
        self.A3 = 0.0
        self.B1 = 0.0
        self.B2 = 0.0
        self.B3 = 0.0
        self.C1 = 0.0
        self.C2 = 0.0
        self.C3 = 0.0


    def printt(self,fo):

        fo.write(int_form(self.cid))
        fo.write(int_form(self.rid))
        fo.write(float_form(self.A1))
        fo.write(float_form(self.A2))
        fo.write(float_form(self.A3))
        fo.write(float_form(self.B1))
        fo.write(float_form(self.B2))
        fo.write(float_form(self.B3))
        fo.write("\n")
        fo.write(float_form(self.C1))
        fo.write(float_form(self.C2))
        fo.write(float_form(self.C3))
        fo.write("\n")


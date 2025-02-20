
#Defines a beam spline for interpolating motion and/or forces for aeroelastic problems on aerodynamic geometries defined by regular arrays of aerodynamic points

class SPLINE2

    def __init__(self):
        self.eid = 0  #unique spline identification number
        self.caero = 0 #aero panel or body that is to be interpolated
        #first and last box or body element whose motions are interpolated using this spline
        self.id1 = 0
        self.id2 = 0
        self.setg = 0 #refers to an SETi entry that lists teh structural grid points to which the spline is attached
        self.dz = 0.0 #linear attachment flexibility
        self.dtor = 1.0 #Torsional flexibility ratio (EI/GJ)
        self.cid 0 # rectangular coordinate system for which the y-axis defines the axis of the spline (not used for bodies)


        #rotational attachment flexibility
        self.dthx = 0.0  #rotation about the spline x-axis(in plane bending) (not for bodies)
        self.dthy = 0.0  #rotation about the spline's y-axis(torsion) used for the slope of bodies
        self.usage = 'FORCE' #FORCE, DISP or BOTH (spline usage flag to determine whether this spline applies to the force transformation, displacment transformation or both



    def printt(self,fo):

        fo.write(int_form(self.eid))
        fo.write(int_form(self.caero))
        fo.write(int_form(self.id1))
        fo.write(int_form(self.id2))
        fo.write(int_form(self.setg))
        fo.write(float_form(self.dz))
        fo.write(float_form(self.dtor))
        fo.write(int_form(self.cid))

        fo.write("\n")

        fo.write(str_form('        '))
        fo.write(float_form(self.dthx))
        fo.write(float_form(self.dthy))
        
        fo.write(str_form('        '))
        fo.write(str_form(self.dthx))
        
        fo.write("\n")



#Defines a set of structural grid points or element identification numbers

class SET1

    def __init__(self):

        self.sid = 0
        self.id = []
        self.no_of_id = 0


    #can specify the list of grid points or thru

    def printt(self,fo):
        fo.write(int_form(self.sid))






#Defines and aerodynamic macro element panel in terms of two leading edge locations and side chords. Used for Double Lattice theory for subsonic aerodynamics and ZONA%! theory for supersonic aerodynamics

class CAERO1

    def __init__(self):

        self.eid = 0  #element identification number
        self.pid = 0  #Property identification number of a PAERO entry. used to specify associated bodies (required)
        self.cp  = 0  #coordinate system for locating points 1 and 4
        self.nspan = 0 # no of spanwise boxes if specified equal divisions are assumed, if 0 or blank , division points given in LSPAN , field 7
        self.nchord = 0 #no of chordwise boxes
        self.lspan = 0 #id of an AEFACT entry containing a list of division boxes for spanwise boxes
        self.lchord = 0 #id of an AEFACT entry containing a list of division boxes for chordwise boxes
        self.igid = 0 #Interference group identification ; aero elements with different igids are uncoupled
        
        #locations of points 1 and 4 in CP coordinate system (outward points)
        
        self.x1 = 0.0
        self.y1 = 0.0
        self.z1 = 0.0
        self.x4 = 0.0
        self.y4 = 0.0
        self.z4 = 0.0
        self.z4 = 0.0
        
        
        #edge chord lengths in aerodynamic coordinate system (chords)
        
        self.x12 = 0.0

        self.x43 = 0.0




    def printt(self,fo):

        fo.write(int_form(self.eid))
        fo.write(int_form(self.pid))
        fo.write(int_form(self.cp))
        fo.write(int_form(self.nspan))
        fo.write(int_form(self.nchord))
        fo.write(int_form(self.lspan))
        fo.write(int_form(self.lchord))
        fo.write(int_form(self.igid))
        fo.write("\n")
        fo.write(float_form(self.x1))
        fo.write(float_form(self.y1))
        fo.write(float_form(self.z1))
        fo.write(float_form(self.x12))
        fo.write(float_form(self.x4))
        fo.write(float_form(self.y4))
        fo.write(float_form(self.z4))
        fo.write(float_form(self.x43))
        
        fo.write("\n")



#----------------------------------------------------------------------------------------

#AEFACT entries for aeroelastic analysis

class AEFACT

    def __init__(self):

        self.sid = 0
        self.no_of_points = 0
        self.d = []



    def printt(self,fo):

        fo.write(int_form(self.sid))
            
            #incorrect fix this here for this case
        
            loc_row_count = (self.no_of_points)/7
            rem_elem = dresp2_list[i].no_of_resp - 7*loc_row_count
                
            curr_pos=0
            for nrow in range(0,loc_row_count):
                
                if(nrow!=0):
                    fo.write(str_form('        '));
                    fo.write(str_form('        '));
                
                for ncol in range(0,7):
                    fo.write(int_form(dresp2_list[i].nr[7*nrow +ncol]));
                    curr_pos =7*nrow +ncol
                
                fo.write("\n");
            
            
            if (curr_pos!=0):
                fo.write(str_form('        '));
                fo.write(str_form('        '));
                for ncol in range(0,rem_elem+1):
                    fo.write(int_form(dresp2_list[i].nr[curr_pos+ncol]));
                fo.write("\n");
        
        



# Defines associated bodies for panels in the doublet lattice method
class PAERO1

    def __init__(self):
        self.pid = 0  #property identification number referenced by CAERO1
        self.b = []   # identification fo CAERO2 entry
        self.no_of_b = 0


    def printt(self):
        fo.write(int_form(self.pid))
        for i in range(0,self.no_of_b):
            fo.write(int_form(self.b[i]))













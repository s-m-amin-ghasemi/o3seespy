from o3seespy.command.nd_material.base_material import NDMaterialBase


class PlaneStressUserMaterial(NDMaterialBase):

    def __init__(self, osi, fc, ft, fcu, epsc0, epscu, epstu, stc):
        self.fc = float(fc)
        self.ft = float(ft)
        self.fcu = float(fcu)
        self.epsc0 = float(epsc0)
        self.epscu = float(epscu)
        self.epstu = float(epstu)
        self.stc = float(stc)
        osi.n_mats += 1
        self._tag = osi.mats
        self._parameters = [self.op_type, self._tag, self.fc, self.ft, self.fcu, self.epsc0, self.epscu, self.epstu, self.stc]
        self.to_process(osi)


class PlateFromPlaneStress(NDMaterialBase):

    def __init__(self, osi, newmat, mat, outof_plane_modulus):
        self.newmat = newmat.tag
        self.mat = mat.tag
        self.outof_plane_modulus = float(outof_plane_modulus)
        osi.n_mats += 1
        self._tag = osi.mats
        self._parameters = [self.op_type, self._tag, self.newmat.tag, self.mat.tag, self.outof_plane_modulus]
        self.to_process(osi)


class PlateRebar(NDMaterialBase):

    def __init__(self, osi, newmat, mat, sita):
        self.newmat = newmat.tag
        self.mat = mat.tag
        self.sita = float(sita)
        osi.n_mats += 1
        self._tag = osi.mats
        self._parameters = [self.op_type, self._tag, self.newmat.tag, self.mat.tag, self.sita]
        self.to_process(osi)

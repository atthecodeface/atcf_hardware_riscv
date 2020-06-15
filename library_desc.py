import cdl_desc
from cdl_desc import CdlModule, CdlSimVerilatedModule, CModel, CSrc

class Library(cdl_desc.Library):
    name="riscv"
    pass

class ReveR(cdl_desc.Modules):
    name = "reve_r"
    c_src_dir    = "cmodel"
    src_dir      = "cdl"
    tb_src_dir   = "tb_cdl"
    libraries = {"std":True, "apb":True, "video":True, "utils":True, "jtag":True, "i2c":True, "io":True, "ethernet":True, "reve_r":True, "networking":True, "crypto":True}
    cdl_include_dirs = ["cdl"]
    export_dirs = cdl_include_dirs + [ src_dir ]
    modules = []
    # modules += [ CdlModule("reve_r_alu") ]
    pass


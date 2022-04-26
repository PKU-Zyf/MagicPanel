# 以下为MagicPanel库的示例代码。
# 访问 https://github.com/pku-zyf/MagicPanel/，可在“example-data”文件夹获取本示例代码用到的原始数据。
# 将“example-data”文件夹复制到本示例代码所在的路径，即可运行。
# 所有数据仅供示例使用，无任何实际意义。

import MagicPanel
from os.path import dirname, join, realpath

def main():
    # 获取原始数据所在路径。
    path = join(dirname(realpath(__file__)), "example-data")
    # 导入“人均GDP”数据（横向）。
    pn1 = (
        MagicPanel
        .QuasiPanel()
        .import_from_csv(path=path, filename="gdppc-horizonal-gbk", encoding="gb18030")
        .standardize_hor(index_row=0, unit_col=0, var_col=1, first_time_col=2)
        .gen_panel()
    )
    # 导入“人口”数据（纵向）。
    pn2 = (
        MagicPanel
        .QuasiPanel()
        .import_from_csv(path=path, filename="pop-vertical-utf8", encoding="utf8")
        .standardize_ver(index_row=2, unit_col=0, time_col=1, first_var_col=2)
        .gen_panel()
    )
    # 导入“人才政策”数据（虚拟变量）。
    pn3 = (
        MagicPanel
        .QuasiPanel()
        .import_from_csv(path=path, filename="policy-big5", encoding="big5")
        .standardize_policy(varname="人才政策", start=2011, end=2020, mode="diac")
        .gen_panel()
    )
    # 导入“专利数量”数据（横向）。
    pn4 = (
        MagicPanel
        .QuasiPanel()
        .import_from_csv(path=path, filename="patent-horizonal-gbk", encoding="gbk")
        .standardize_hor(index_row=1, unit_col=0, var_col=None, var_name="专利数量", first_time_col=1)
        .gen_panel()
    )
    # 导入“专利数量”补充数据（横向）。
    pn5 = (
        MagicPanel
        .QuasiPanel()
        .import_from_csv(path=path, filename="patent-horizonal-sup-gbk", encoding="gbk")
        .standardize_hor(index_row=1, unit_col=0, var_col=None, var_name="专利数量", first_time_col=1)
        .gen_panel()
    )    
    # 合并数据。
    pn = (
        pn1
        .absorb(pn2)
        .absorb(pn3)
        .absorb(pn4)
        .absorb(pn5, mode="complementary", mapping={"专利数量": "专利数量"})
        .sort()
    )
    # 导出数据。导出为gb18030格式，可在Windows系统的Excel中直接打开。
    pn.export(path=path, filename="result", encoding="gb18030")

if __name__ == "__main__":
    main()

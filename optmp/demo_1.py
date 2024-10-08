from ray_tracing import *

# Build Lens system by adding surfaces, wavelengths, fields

# 创建透镜组New_Lens
New_Lens = lens.Lens(lens_name='Triplet',creator='L')
New_Lens.FNO = 5
New_Lens.lens_info()  

New_Lens.add_wavelength(wl = 656.30)
New_Lens.add_wavelength(wl = 587.60)
New_Lens.add_wavelength(wl = 486.10)
New_Lens.list_wavelengths()

New_Lens.add_wavelength(wl = 700)
New_Lens.add_wavelength(wl = 600)
New_Lens.add_wavelength(wl = 500)
New_Lens.list_wavelengths()

# 创建光场
New_Lens.add_field_YAN(angle=0)
New_Lens.add_field_YAN(angle=10)
New_Lens.add_field_YAN(angle=30)
New_Lens.list_fields()

# 添加平面
New_Lens.add_surface(number=1,radius=10000000,thickness=1000000,glass='air',output=True)
New_Lens.add_surface(number=2,radius=41.15909,thickness=6.097555 ,glass='S-BSM18_ohara',output=True)
New_Lens.add_surface(number=3,radius=-957.83146,thickness=9.349584,glass='air',output=True)
New_Lens.add_surface(number=4,radius=-51.32104,thickness=2.032518,glass='N-SF2_schott',output=True)
New_Lens.add_surface(number=5,radius=42.37768 ,thickness=5.995929 ,glass='air',output=True)
New_Lens.add_surface(number=6,radius=10000000,thickness=4.065037,glass='air',STO=True,output=True)
New_Lens.add_surface(number=7,radius=247.44562,thickness=6.097555,glass='S-BSM18_ohara',output=True)
New_Lens.add_surface(number=8,radius=-40.04016,thickness=85.593426,glass='air',output=True)
New_Lens.add_surface(number=9,radius=10000000,thickness=0,glass='air',output=True)

New_Lens.add_surface(number=4,radius=10000000,thickness=0,glass='air',output=True)

# first do refresh_paraxial function find entrace pupil position
New_Lens.refresh_paraxial()

# Trace ray through system, draw lens system
dict_list = trace.trace_draw_rays(New_Lens)
draw.draw_system(New_Lens)
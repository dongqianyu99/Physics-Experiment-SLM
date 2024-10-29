from ray_tracing import *

New_Lens = lens.Lens(lens_name='Doublegauss',creator='L')
New_Lens.FNO = 5
New_Lens.lens_info()

New_Lens.add_wavelength(wl = 656.30)
New_Lens.add_wavelength(wl = 587.60)
New_Lens.add_wavelength(wl = 486.10)

New_Lens.add_field_YAN(angle=0)
New_Lens.add_field_YAN(angle=10)
New_Lens.add_field_YAN(angle=14)

New_Lens.add_surface(number=1,radius=10000000,thickness=1000000,glass='air')
New_Lens.add_surface(number=2,radius=50,thickness=10,glass='N-SSK2_schott') 
New_Lens.add_surface(number=3,radius=80,thickness=100,glass='air',STO=True)
New_Lens.add_surface(number=4,radius=10000000,thickness=0,glass='air')

# New_Lens.add_surface(number=1,eccentricity=1,thickness=1000000,glass='air')
# New_Lens.add_surface(number=2,eccentricity=1.5,thickness=10,glass='N-SSK2_schott') 
# New_Lens.add_surface(number=3,eccentricity=2,thickness=100,glass='air',STO=True)
# New_Lens.add_surface(number=4,eccentricity=1,thickness=0,glass='air')

New_Lens.refresh_paraxial()
New_Lens.solve_imageposition()
trace.trace_draw_rays(New_Lens)
draw.draw_system(New_Lens)


try:
    print("Checking if Pint is installed...")
    from pint import UnitRegistry

except:
    print("Pint is not installed.")
    print("Installing using pip magic command - this may take a few moments...")
    %pip -v install pint
    from pint import UnitRegistry

finally:
    print("Pint is installed and ready!")
    p = UnitRegistry(autoconvert_offset_to_baseunit = True)
    p.default_format = '.1f~P'

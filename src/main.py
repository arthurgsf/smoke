import utils

if __name__ == "__main__":
    smoke = utils.load_imgs("../data/USTC_SmokeRS/Smoke/*.tif")
    dust = utils.load_imgs("../data/USTC_SmokeRS/Dust/*.tif")
    haze = utils.load_imgs("../data/USTC_SmokeRS/Haze/*.tif")
    land = utils.load_imgs("../data/USTC_SmokeRS/Land/*.tif")
    seaside = utils.load_imgs("../data/USTC_SmokeRS/Seaside/*.tif")
    cloud = utils.load_imgs("../data/USTC_SmokeRS/Cloud/*.tif")
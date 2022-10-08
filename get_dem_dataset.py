from pathlib import Path
import pandas as pd
import geopandas as gpd


def get_dem_dataset():
    path = Path("./data/DEM/서울특별시/2014 서울특별시[ascii]")
    dem = []
    for p in path.glob("*.txt"):
        dem.append(pd.read_csv(p, sep=" ", header=None))

    dem = pd.concat(dem).reset_index(drop=True)
    dem.columns = ["x", "y", "z"]
    dem = gpd.GeoDataFrame(
        data=dem.z,
        geometry=gpd.points_from_xy(x=dem.x, y=dem.y),
        crs="EPSG:5186",  # 아놔..
    )
    dem = dem.to_crs("EPSG:4326")

    return dem

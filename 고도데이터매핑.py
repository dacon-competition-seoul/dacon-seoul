# %%
import pandas as pd
import geopandas as gpd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
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

    df = pd.read_csv(
        "data/따릉이대여소위치/3. 공공자전거 대여소 정보(22.06월 기준).csv", encoding="cp949", skiprows=4
    )
    df.columns = [
        "id",
        "name",
        "gu",
        "loc",
        "y",
        "x",
        "ds",
        "isLCD",
        "slot",
        "isQR",
    ]
    df = df.drop(["isLCD", "isQR"], axis=1)

    x_std, y_std = df.x.std(), df.y.std()

    x_candidates: np.ndarray = dem.geometry.x.values
    y_candidates: np.ndarray = dem.geometry.y.values

    df_chunks = []
    for i in range(0, 2500, 500,):
        df_chunk = df[i : i + 500].reset_index(drop=True)
        x = df_chunk.x.values.reshape(-1, 1)
        y = df_chunk.y.values.reshape(-1, 1)
        indices = np.argmin(
            np.abs(x - x_candidates) / x_std + np.abs(y - y_candidates) / y_std, axis=-1
        )
        df_chunk["dem"] = dem.loc[indices, "z"].values
        df_chunks.append(df_chunk)

    df = pd.concat(df_chunks)

    df

    df.to_csv("서울시_따릉이대여소별_고도데이터.csv", index=False)

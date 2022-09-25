from glob import glob
import json
from pathlib import Path
import pandas as pd


def main():

    __dirname = Path(__file__).parent
    dfs = []
    for p in __dirname.joinpath("../서울_경찰서별_5대범죄_통계").glob("*.csv"):
        temp = pd.read_csv(p, encoding="cp949").dropna()
        if "검거" in temp.columns:
            temp = temp.rename(columns={"검거": "건수"})

        year = str(p)[-8:-4]

        temp["year"] = [year for _ in range(len(temp))]

        dfs.append(temp)

    df = pd.concat(dfs).iloc[:, :5]
    df = df.sort_values("year").reset_index(drop=True)

    with open(
        __dirname.joinpath("../지역별관할경찰서/경찰서별관할구역.json"), "r", encoding="utf-8"
    ) as f:
        juridict1 = json.load(f)
    with open(
        __dirname.joinpath("../지역별관할경찰서/지역별관할경찰서.json"), "r", encoding="utf-8"
    ) as f:
        juridict2 = json.load(f)

    df["관할구역"] = df["구분"].map(lambda x: juridict1[x])
    df = df.groupby(["year", "관할구역", "죄종", "발생검거",]).sum()
    df = df.reset_index()
    df = df.rename(columns={"관할구역": "자치구"})
    df["관할경찰서"] = df["자치구"].map(lambda x: juridict2[x])
    df["건수"] = df["건수"].astype(int)

    df["죄종"] = df["죄종"].replace("강간", "강간,추행")
    df.to_csv(__dirname.joinpath("01-20_자치구별_5대범죄.csv"), index=False)


if __name__ == "__main__":
    main()

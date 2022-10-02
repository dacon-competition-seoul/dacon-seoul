import pandas as pd
from pathlib import Path


def main():
    __dirname = Path(__file__).parent
    df = pd.concat(
        [
            pd.read_csv(
                __dirname.joinpath("경찰청_전국 경찰서별 경찰관 현황_12_31_2015.csv"),
                encoding="cp949",
            ).rename(columns={" 경찰관 ": "경찰관"}),
            pd.read_csv(
                __dirname.joinpath("경찰청_경찰서별정원_20211014.csv"), encoding="cp949"
            ),
        ]
    )

    df = df[df["지방청"] == "서울"]
    df = df.rename(columns={"년도": "ds", "경찰서": "officeName", "경찰관": "quota"}).drop(
        "지방청", axis=1
    )
    answer = []
    for num in df.quota.to_list():
        try:
            num = int(num)
        except:
            num = num.replace(",", "")
            num = int(num)
        answer.append(num)

    df["quota"] = answer
    df["ds"] = df.ds.str[:4]
    df["officeName"] = df.officeName.str[2:]
    df.to_csv(__dirname.joinpath("2014-2021_서울_경찰서별_정원.csv"), index=False)


if __name__ == "__main__":
    main()

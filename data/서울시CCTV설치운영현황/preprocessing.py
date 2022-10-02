import pandas as pd
from pathlib import Path


def main():
    __dirname = Path(__file__).parent
    df = pd.read_csv(
        __dirname.joinpath("서울시CCTV설치운영현황(자치구)_년도별_211231기준.csv"),
        encoding="cp949",
        skiprows=1,
    )
    df = df.set_index("구분").T
    df = df.drop("총계")
    df = df.drop("계", axis=1)
    df.columns = df.columns.map(lambda x: x.replace(" ", ""))

    df.to_csv(__dirname.joinpath("서울시CCTV연도별신규설치수.csv"))


if __name__ == "__main__":
    main()

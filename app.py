import pandas as pd
import networkx as nx
import streamlit as st


st.set_page_config(
    page_title="metro baazww",
    page_icon="🚇",
    layout="centered"
)

st.markdown("""
<style>

/* ---------- Main background ---------- */

.stApp {
    background:
        radial-gradient(circle at 20% 10%, rgba(55, 65, 81, 0.22), transparent 35%),
        radial-gradient(circle at 80% 90%, rgba(76, 29, 149, 0.16), transparent 35%),
        linear-gradient(135deg, #111827 0%, #151a24 50%, #10151f 100%);

    color: #f3f4f6;
}


/* ---------- Center everything ---------- */

.block-container {
    max-width: 850px;
    margin: auto;
    text-align: center;
}


/* ---------- Title ---------- */

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}


/* ---------- Subtitle ---------- */

.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 17px;
    margin-bottom: 35px;
}


/* ---------- Station Card ---------- */

.station {
    width: 100%;
    box-sizing: border-box;

    text-align: center;

    font-size: 20px;
    font-weight: 700;

    padding: 14px 18px;
    margin: 8px 0;

    border-radius: 14px;

    background: rgba(31, 41, 55, 0.42);

    border: 1px solid rgba(255, 255, 255, 0.08);

    box-shadow:
        0 4px 15px rgba(0, 0, 0, 0.12);

    backdrop-filter: blur(10px);

    transition: 0.2s;
}


.station:hover {
    transform: translateY(-2px);

    background: rgba(55, 65, 81, 0.5);

    border-color: rgba(255, 255, 255, 0.14);

    box-shadow:
        0 7px 22px rgba(0, 0, 0, 0.2);
}


/* ---------- Arrow ---------- */

.arrow {
    width: 100%;
    text-align: center;

    color: #6b7280;

    font-size: 20px;

    margin: 2px 0;
}


/* ---------- Transfer ---------- */

.change {
    width: 100%;
    box-sizing: border-box;

    text-align: center;

    background: rgba(120, 82, 20, 0.18);

    border: 1px solid rgba(245, 158, 11, 0.45);

    border-radius: 14px;

    padding: 14px 15px;

    margin: 10px 0;

    color: #fbbf24;

    font-weight: bold;

    backdrop-filter: blur(10px);

    box-shadow:
        0 4px 18px rgba(245, 158, 11, 0.08);
}


/* ---------- Info ---------- */

.info {
    width: 100%;
    box-sizing: border-box;

    text-align: center;

    padding: 15px;

    border-radius: 14px;

    background: rgba(31, 41, 55, 0.55);

    border: 1px solid rgba(255, 255, 255, 0.06);

    margin-top: 20px;

    backdrop-filter: blur(10px);
}


/* ---------- Inputs ---------- */

div[data-baseweb="input"] {
    background: rgba(31, 41, 55, 0.55);

    border-radius: 10px;
}


/* ---------- Input text ---------- */

input {
    text-align: center !important;
}


/* ---------- Input labels ---------- */

label {
    text-align: center !important;
}


/* ---------- Selectbox ---------- */

div[data-baseweb="select"] {
    background: rgba(31, 41, 55, 0.55);

    border-radius: 10px;

    border: 1px solid rgba(255, 255, 255, 0.06);
}


/* ---------- Selectbox text ---------- */

div[data-baseweb="select"] div {
    text-align: center;
}


/* ---------- Button ---------- */

.stButton > button {
    border-radius: 12px;

    border: 1px solid rgba(255, 255, 255, 0.08);

    background: rgba(31, 41, 55, 0.75);

    color: #f3f4f6;

    font-size: 17px;
    font-weight: 700;

    padding: 10px;

    transition: 0.2s;
}


.stButton > button:hover {
    background: rgba(55, 65, 81, 0.9);

    border-color: rgba(255, 255, 255, 0.15);
}


/* ---------- Success message ---------- */

div[data-testid="stAlert"] {
    text-align: center;

    border-radius: 12px;
}


/* ---------- Warning / Error ---------- */

div[data-testid="stAlert"] p {
    text-align: center;
}


/* ---------- Route title ---------- */

h3 {
    text-align: center;
}


/* ---------- Horizontal line ---------- */

hr {
    border-color: rgba(255, 255, 255, 0.08);
}

</style>
""", unsafe_allow_html=True)


def esm(x, lst):

    ln = 1
    score = 0
    lt = []

    for i in lst:

        ln = abs(len(x) - len(str(i)))

        ln2 = 0
        com = 0

        for j in range(min(len(x), len(i))):

            if x[j] == i[j]:
                ln2 += 1

        for char in x:

            if char in i:
                com += 1

        score = ln - ln2 - com

        lt.append((i, score))

    lt.sort(key=lambda x: x[1])

    return lt[0][0]


colors = {

    "l1": "#ff2b2b",
    "l2": "#0066ff",
    "l3": "#00d9d9",
    "l4": "#ffd500",
    "l5": "#00c853",
    "l6": "#ff69b4",
    "l7": "#9b59ff"

}


df = pd.read_excel("station.xlsx")

stations = df.stack().dropna().tolist()

G = nx.Graph()

lines = [
    "l1",
    "l2",
    "l3",
    "l4",
    "l5",
    "l6",
    "l7"
]

for line in lines:

    lst = df[line].dropna().tolist()

    for i in range(len(lst) - 1):

        G.add_edge(
            lst[i],
            lst[i + 1]
        )


st.markdown(
    '<div class="title">🚇 Tehran Metro</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">  masiryaabi</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)

with col1:

    start_input = st.selectbox(
        "where are you???",
        options=[""] + stations,
        index=0,
        placeholder="example : tajrish"
    )

with col2:

    end_input = st.selectbox(
        "where do you want to go???",
        options=[""] + stations,
        index=0,
        placeholder="example : meydane enghelab"
    )


find_route = st.button(
    "Agha Arshia, find a route for me",
    use_container_width=True
)


if find_route:

    if not start_input or not end_input:

        st.warning("Please enter your starting point and destination.")

    else:

        start = esm(start_input, stations)
        end = esm(end_input, stations)

        try:

            path = nx.shortest_path(
                G,
                start,
                end
            )

            line = []
            taviz = []

            for i in range(len(path)):

                line.append(
                    df.columns[
                        df.eq(path[i]).any()
                    ].tolist()
                )


            if len(line[0]) == 2:

                if len(line[1]) == 1:

                    line[0] = line[1]

                else:

                    x = list(
                        set(line[0]).intersection(line[1])
                    )

                    line[0] = x


            if len(line[-1]) == 2:

                if len(line[-2]) == 1:

                    line[-1] = line[-2]

                else:

                    x = list(
                        set(line[-1]).intersection(line[-2])
                    )

                    line[-1] = x


            for i in range(len(line)):

                if len(line[i]) == 2:

                    if line[i - 1] != line[i + 1]:

                        taviz.append(path[i])


            for i in range(len(line)):

                lss = []

                if len(line[i]) == 2:

                    lss.append(line[i][0])

                    line[i] = lss


            st.success(
                f"AghaArshia finds a route : {start} → {end}"
            )

            st.markdown(
                f"""
                <div class="info">
                    🚉 stations: <b>{len(path)}</b>
                    &nbsp;&nbsp; | &nbsp;&nbsp;
                    🔄 transfers: <b>{len(taviz)}</b>
                </div>
                """,
                unsafe_allow_html=True
            )


            st.markdown("### 🗺️ route:")


            for i in range(len(path)):

                station = path[i]

                if station in taviz:

                    st.markdown(
                        f"""
                        <div class="change">
                            🔄 change in:
                            <b>{station}</b>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    color = colors[line[i][0]]

                    st.markdown(
                        f"""
                        <div class="station"
                             style="
                             color:{color};
                             border-color:{color}55;
                             box-shadow:
                             0 4px 18px {color}18;
                             ">
                            🚉 {station}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                if i < len(path) - 1:

                    st.markdown(
                        '<div class="arrow">↓</div>',
                        unsafe_allow_html=True
                    )


            st.markdown("---")

            st.markdown(
                f"""
                <div class="info">

                🚇 <b>starting point:</b>
                <span style="color:{colors[line[0][0]]}">
                {line[0][0]}
                </span>

                <br><br>

                🔄 <b>changes:</b>
                {len(taviz)}

                <br><br>

                🚉 <b>stations:</b>
                {len(path)}

                </div>
                """,
                unsafe_allow_html=True
            )


        except nx.NetworkXNoPath:

            st.error(
                "sorry i can't find a route"
            )

        except Exception as e:

            st.error(
                f"error: {e}"
            )

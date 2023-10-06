{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqd8X9QxmgpmcLW9SeC5pO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MukeshMishraReloaded/mc_streamlit/blob/main/yulu.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "id": "XAZ5MTKQ4aEX"
      },
      "outputs": [],
      "source": [
        "import datetime\n",
        "import streamlit as st\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "import pandas as pd\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_yulu = pd.read_csv(\"https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/428/original/bike_sharing.csv?1642089089\")"
      ],
      "metadata": {
        "id": "tox4oHBj5l2g"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.write(\"\"\"\n",
        "            # Yulu data analyzer \"\"\")\n",
        "\n",
        "## get data for Yulu bikes\n",
        "\n",
        "season = st.selectbox(\n",
        "    'Which season do you want to analyse?',\n",
        "    ('1', '2', '3', '4'))\n",
        "\n",
        "col1, col2 = st.columns(2)\n",
        "\n",
        "st.dataframe(df_yulu['season'].unique())\n",
        "\n",
        "df=df_yulu\n",
        "\n",
        "st.write(f\"\"\"\n",
        "    ###  Season {season}'s - renting of bikes data \"\"\")\n",
        "\n",
        "st.dataframe(df[df['season'] == 1][['casual', 'registered', 'count']])\n",
        "\n",
        "st.write(f\"\"\"\n",
        "    ### Season {season}'s - renting of bikes data\"\"\")\n",
        "\n",
        "st.line_chart(df[df['season'] == season]['count'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9YVvR0pL5jDK",
        "outputId": "c81de990-3d3b-4d21-924f-7971baea86ce"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    }
  ]
}
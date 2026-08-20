@echo off
title Second Brain Agent
echo ==========================================
echo Starting Second Brain Agent...
echo ==========================================
pip install -r requirements.txt
streamlit run app.py
pause

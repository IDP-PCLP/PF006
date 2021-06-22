#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PF006

Objetivos:
- Desenvolver uma calculadora que pegue os dados da empresa(pode ser no excel) e faça os cálculos de acordo com alguns inputs dados pelo usuário,
- Implementar uma simulação de Monte Carlo.
"""


import pandas as pd
import numpy as np

avg = 0.1
std_dev = .05
num_reps = 500
num_simulations = 10
Tc = np.random.normal(avg, std_dev, num_reps).round(2)
wacc = 0.085+1
G = 0.03
Fc = 1500

def valor_terminal(Fc,Tc,wacc,G):
    # Valor Terminal(Vt)= Fc5*Tc/ WACC - G
    return Fc*Tc/wacc -G
def fluxo_caixa_descontado(Fc,Tc,wacc,Vt):
    # Fluxo de Caixa Descontado=SOMA(Fc*Tc/WACC) + Vt
    return sum(Fc*Tc/wacc) + Vt

# Define a list to keep all the results from each simulation that we want to analyze
all_stats = []

# Loop through many simulations
for i in range(num_simulations):
    TcAtual = np.random.choice(Tc)
    Vt = valor_terminal(Fc,TcAtual,wacc,G)
    Fc = fluxo_caixa_descontado(Fc,Tc,wacc,Vt)
    all_stats.append([Vt,Fc])
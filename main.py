from module_decide_holding_stocks import decide_holding_stocks
from module_decide_candidates import scan_candidates
import pandas as pd

frame = pd.read_csv('Candidates_CSI300.csv')

def scan_decide():
    decision_holding_stocks = decide_holding_stocks()
    decision_candidates = scan_candidates(frame)
    
    print(decision_holding_stocks)
    print(decision_candidates)
    
    return

if __name__ == '__main__':
    scan_decide()
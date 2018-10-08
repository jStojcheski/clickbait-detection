def conf_mtx(df, t):
    df = pd.concat([(df.sum(axis=1) >= df.shape[1] / 2), t], axis=1)
    df.columns=['y', 't']
    
    pos = df[df['t'] == True]
    neg = df[df['t'] == False]

    tp = (pos['y'] == True).sum()
    fn = (pos['y'] == False).sum()
    fp = (neg['y'] == True).sum()
    tn = (neg['y'] == False).sum()
    
    print('TP:', tp)
    print('FN:', fn)
    print('FP:', fp)
    print('TN:', tn, end='\n\n')

    print('Accuracy:', ((tp + tn) / (tp + fn + fp + tn) * 100).round(dec), end='\n\n')
    
    prec = (tp / (tp + fp))
    rcll = (tp / (tp + fn))
    f1   = 2 * (prec * rcll) / (prec + rcll)

    print('Precision:', prec.round(dec))
    print('Recall:',rcll.round(dec))
    print('F1-score:', f1.round(dec))
    
    return tp, fn, fp, tn
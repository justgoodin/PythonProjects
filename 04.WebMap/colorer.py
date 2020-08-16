def colour(el,mean):
    if el <mean//2 :       
        color = 'green'
    elif mean//2 <= el < 3*mean//2:
        color = "orange"
    else:
        color = 'red'
    return color
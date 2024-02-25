def Physics(unit):
    if unit=='kinematics':
        a=input('a?: ')
        v_i=input('v_i?: ')
        v_f=input('v_f?: ')
        t=input('t?: ')
        d=input('d?: ')
        if a=='None' and t=='None':
            a=0
            a=a+((float(v_f))**2-(float(v_i))**2)/(2*float(d))
            t=0
            t=t+((2*float(d))/(float(v_f)+float(v_i)))
        if a=='None' and d=='None':
            a=0
            a=a+((float(v_f)-float(v_i))/float(t))
            d=0
            d=d+((float(v_f)+float(v_i))*.5*float(t))
        if a=='None' and v_i=='None':
            a=0
            t=float(t)
            v_f=float(v_f)
            d=float(d)
            a=a+((2*(v_f*t-d))/(t)**2)
            v_i=0
            v_i=v_i+(((2*float(d))/float(t))-float(v_f))
        if a=='None' and v_f=='None':
            v_i=float(v_i)
            d=float(d)
            t=float(t)
            a=0
            a=a+((2*(d-v_i*t))/(t**2))
            v_f=0
            v_f=v_f+(((2*d)/t)-v_i)
        if v_f=='None' and v_i=='None':
            d=float(d)
            a=float(a)
            t=float(t)
            v_f=0
            v_f=v_f+((d+.5*a*(t**2))/(t))
            v_i=0
            v_i=v_i+((d-.5*a*(t**2))/(t))
        if v_i=='None' and d=='None':
            v_f=float(v_f)
            t=float(t)
            a=float(a)
            v_i=0
            v_i=v_i+(v_f-(a*t))
            d=0
            d=d+(v_f*t-.5*a*(t**2))
        if v_i=='None' and t=='None':
            v_f=float(v_f)
            d=float(d)
            a=float(a)
            v_i=0
            v_i=v_i+((v_f**2)-(2*a*d))**.5
            t_1=0
            t_2=0
            t_1=(((v_f)-(v_i))/a)
            t_2=(((v_f)+(v_i))/a)
            t=f'{t_1} and {t_2}'
        if v_f=='None' and t=='None':
            d=float(d)
            v_i=float(v_i)
            a=float(a)
            v_f=0
            v_f=v_f+(((v_i)**2)+(2*a*d))**.5
            t_1=0
            t_2=0
            t_1=(((v_i)-(v_f))/(-1)*a)
            t_2=(((v_i)+(v_f))/(-1)*a)
            t=f'{t_1} and {t_2}'
        if t=='None' and d=='None':
            v_f=float(v_f)
            v_i=float(v_i)
            a=float(a)
            t=0
            t=t+((v_f-v_i)/a)
            d=0
            d=d+((v_f**2-v_i**2)/(2*a))
        if v_f=='None' and d=='None':
            v_i=float(v_i)
            t=float(t)
            a=float(a)
            v_f=0
            v_f=v_f+(v_i+a*t)
            d=0
            d=d+((v_i*t)+(.5*a*(t**2)))
        return print(f'The acceleration is {a} m/s^2, the time is {t} second(s), the initial velocity is {v_i} m/s, the final velocity is {v_f} m/s, and the displacement is {d} meters.')
Physics('kinematics')
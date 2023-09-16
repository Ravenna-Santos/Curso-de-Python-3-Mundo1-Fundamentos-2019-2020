s = float(input('Digite o salário: '))
if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15
print('O salário após o aumento é R$: {:.2f}'.format(s))

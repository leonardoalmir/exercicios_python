print("=========== DESAFIO 014 =============\n"
      "Escreva um programa que converta uma \n"
      "temperatura digitada em graus °C (celsius)\n"
      "para °F (fahrenheit). \n"
      "=====================================\n")
tempC = float(input("Digite a temperatura em °C: "))
tempF = ((tempC * 9) / 5) + 32

print("A temperatura de {:.1f}°C em fahrenheit é: {:.1f}°F.".format(tempC, tempF))
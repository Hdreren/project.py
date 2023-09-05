import matplotlib.pyplot as plt

# plt.xkcd()

print(plt.style.available)

### Hazır stil kullanımı
# plt.style.use('bmh')
# plt.style.use('classic')
plt.style.use('dark_background')

x_ekseni=[1,2,3,4,5]
y_AliReza=[45,55,65,63,120]
y_Gulu=[10,25,35,40,45]
y_Altan=[65,85,95,105,145]

plt.title("Yas-Boy Tablosu")
plt.xlabel("Yaşlar")
plt.ylabel("Boylar")



## El ile stil verme
# plt.plot(x_ekseni,y_Fatma,color="b",linestyle="--",marker="x",label="Fatma")
# plt.plot(x_ekseni,y_Eren,"ko-",label="Eren")
# plt.plot(x_ekseni,y_Kenan,color="#f54245",linestyle="-.",marker=".",label="Kenan")


# otomatik stil kullanımı
plt.plot(x_ekseni,y_Fatma,label="Fatma")
plt.plot(x_ekseni,y_Eren,label="Eren")
plt.plot(x_ekseni,y_Kenan,label="Kenan")


# plt.bar(x_ekseni,y_Kenan,label="Kenan")
# plt.bar(x_ekseni,y_Fatma,label="Fatma")
# plt.bar(x_ekseni,y_Eren,label="Eren")



plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
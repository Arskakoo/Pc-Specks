import urllib.request
import speedtest
import subprocess

def testaa_internet_yhteys():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        print("Internet-yhteys toimii.")
    except Exception as e:
        print("Internet-yhteys ei toimi. Virhe: ", str(e))

def nopeustesti():
    st = speedtest.Speedtest()
    latausnopeus = st.download() / 10**6  # Megabittejä sekunnissa
    uploadnopeus = st.upload() / 10**6  # Megabittejä sekunnissa

    print(f"Latausnopeus: {latausnopeus:.2f} Mbps")
    print(f"Uploadnopeus: {uploadnopeus:.2f} Mbps")


# Testataan kaikki
testaa_internet_yhteys()
print("\n---\n")
nopeustesti()
print("\n---\n")



# pip install speedtest-cli 

import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt

# Lista de sites
websites = [
    "https://https://developer.hashicorp.com/terraform",
    "https://www.google.com",
    "https://https://www.cisco.com/"
]

# Configurações do Chrome (headless)
options = Options()
options.add_argument('--log-level=3')  # Esconde a maioria dos logs do Chrome
options.add_argument('--disable-logging')  # Tenta silenciar ainda mais
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--enable-unsafe-webgpu")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--enable-unsafe-swiftshader")
driver = webdriver.Chrome(options=options)

# Função para medir o tamanho da página
def get_page_size(url):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)  # espera extra para carregar recursos

        resources = driver.execute_script("""
            return performance.getEntriesByType("resource").map(resource => ({
                name: resource.name,
                transferSize: resource.transferSize || 0
            }));
        """)
        total_size_bytes = sum(r["transferSize"] for r in resources)
        total_size_mb = round(total_size_bytes / (1024 * 1024), 2)
        return total_size_mb, None
    except Exception as e:
        return None, str(e)

# Coleta de dados
resultados = []
for site in websites:
    print(f"Analisando {site}...")
    size_mb, error = get_page_size(site)
    resultados.append({
        "Website": site,
        "Size (MB)": size_mb if size_mb is not None else 0,
        "Error": error if error else ""
    })

driver.quit()

# Salvar CSV
with open("page_sizes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Website", "Size (MB)", "Error"])
    writer.writeheader()
    for r in resultados:
        writer.writerow(r)

# Gerar gráfico com matplotlib
labels = [r["Website"].replace("https://", "").replace("www.", "") for r in resultados]
sizes = [r["Size (MB)"] for r in resultados]

plt.figure(figsize=(12, len(labels) * 0.25 + 3))
bars = plt.barh(labels, sizes, color="#4A90E2")

# Adiciona texto com o valor em cada barra
for bar, size in zip(bars, sizes):
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
             f"{size} MB", va="center", fontsize=8)

plt.xlabel("Tamanho da página (MB)")
plt.title("Tamanho das páginas")
plt.tight_layout()
plt.savefig("grafico.png", dpi=300)
plt.show()

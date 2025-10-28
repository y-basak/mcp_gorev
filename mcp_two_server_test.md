# MCP Servers Project 🚀

Bu proje, **Model Context Protocol (MCP)** kullanarak basit sunucu örnekleri ve test senaryolarını içermektedir. İki farklı MCP sunucusu (Greeting ve Math) ve bunları test eden kapsamlı test dosyaları bulunmaktadır.

## 📋 İçindekiler

- [Proje Yapısı](#proje-yapısı)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Sunucular](#sunucular)
- [Testler](#testler)
- [Kullanım](#kullanım)
- [Test Sonuçları](#test-sonuçları)

## 📁 Proje Yapısı

```
.
├── greeting_mcp_server.py    # Selamlama sunucusu
├── math_mcp_server.py         # Matematik işlemleri sunucusu
├── mcp_client_test.py         # Manuel test istemcisi
└── pytest_tests.py            # Otomatik pytest testleri
```

## 🔧 Gereksinimler

```bash
pip install mcp
pip install pytest pytest-asyncio
```

**Python Sürümü:** Python 3.8+

## 📦 Kurulum

1. Projeyi klonlayın veya indirin
2. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

**requirements.txt içeriği:**
```
mcp
pytest
pytest-asyncio
```

## 🖥️ Sunucular

### 1. Greeting Server (greeting_mcp_server.py)

Basit selamlama mesajları sunan MCP sunucusu.

**Kaynaklar:**
- `resource://greet` - Hoş geldin mesajı
- `resource://farewell` - Veda mesajı

**Örnek Kullanım:**
```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["greeting_mcp_server.py"],
    env=None
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        response = await session.read_resource("resource://greet")
        print(response.contents[0].text)
```

### 2. Math Server (math_mcp_server.py)

Temel matematik işlemleri yapan MCP sunucusu.

**Kaynaklar:**
- `resource://addition` - Toplama işlemi (15 + 27 = 42)
- `resource://multiplication` - Çarpma işlemi (8 × 12 = 96)

**Örnek Kullanım:**
```python
response = await session.read_resource("resource://addition")
print(response.contents[0].text)
# Çıktı: Addition result: 15 + 27 = 42
```

## 🧪 Testler

### Manuel Test İstemcisi (mcp_client_test.py)

Konsol çıktısı ile detaylı test sonuçları gösterir.

**Çalıştırma:**
```bash
python mcp_client_test.py
```

**Test Kapsamı:**
- ✅ Sunucu bağlantı testleri
- ✅ Kaynak okuma testleri
- ✅ Geçersiz kaynak hata testleri
- ✅ Her iki sunucu için tam kapsam

**Örnek Çıktı:**
```
████████████████████████████████████████████████████████████
█                  MCP SERVERS TEST SUITE                   █
████████████████████████████████████████████████████████████

============================================================
TESTING GREETING SERVER
============================================================

✓ Client is connected to Greeting MCP Server

--- Testing greet resource ---
Response: Hello! Welcome to the Greeting Server.

--- Testing farewell resource ---
Response: Goodbye! Thank you for using the Greeting Server.
```

### Otomatik Testler (pytest_tests.py)

Pytest framework'ü ile profesyonel birim testleri.

**Çalıştırma:**
```bash
pytest pytest_tests.py -v -s
```

**Test Listesi:**

#### Greeting Server Testleri:
1. `test_greeting_server_connection` - Bağlantı testi
2. `test_greet_resource` - Greet kaynağı testi
3. `test_farewell_resource` - Farewell kaynağı testi
4. `test_greeting_server_invalid_resource` - Hata yönetimi

#### Math Server Testleri:
5. `test_math_server_connection` - Bağlantı testi
6. `test_addition_resource` - Toplama testi (42 kontrolü)
7. `test_multiplication_resource` - Çarpma testi (96 kontrolü)
8. `test_math_server_invalid_resource` - Hata yönetimi
9. `test_math_both_resources` - Entegrasyon testi

## 🎯 Kullanım

### Manuel Testleri Çalıştırma

```bash
python mcp_client_test.py
```

### Pytest Testlerini Çalıştırma

```bash
# Tüm testler
pytest pytest_tests.py -v -s

# Belirli bir test
pytest pytest_tests.py::test_addition_resource -v -s

# Sadece Greeting Server testleri
pytest pytest_tests.py -k "greeting" -v -s

# Sadece Math Server testleri
pytest pytest_tests.py -k "math" -v -s
```

### Pytest Parametreleri

- `-v` : Verbose (detaylı çıktı)
- `-s` : Print ifadelerini göster
- `-k` : Test ismine göre filtrele
- `--tb=short` : Kısa traceback

## 📊 Test Sonuçları

Başarılı bir test çalışması şu çıktıyı üretir:

```
pytest pytest_tests.py -v -s

========================= test session starts =========================
collected 9 items

pytest_tests.py::test_greeting_server_connection PASSED
pytest_tests.py::test_greet_resource PASSED
pytest_tests.py::test_farewell_resource PASSED
pytest_tests.py::test_greeting_server_invalid_resource PASSED
pytest_tests.py::test_math_server_connection PASSED
pytest_tests.py::test_addition_resource PASSED
pytest_tests.py::test_multiplication_resource PASSED
pytest_tests.py::test_math_server_invalid_resource PASSED
pytest_tests.py::test_math_both_resources PASSED

========================= 9 passed in 2.34s ==========================
```

## 🔍 Test Detayları

### Greeting Server Testleri

| Test | Kontrol Edilen | Beklenen Sonuç |
|------|----------------|----------------|
| Connection | Sunucu bağlantısı | Session oluşturulmalı |
| Greet | "Hello" ve "Greeting Server" | Mesajda bulunmalı |
| Farewell | "Goodbye" ve "Greeting Server" | Mesajda bulunmalı |
| Invalid | Geçersiz kaynak | Exception fırlatmalı |

### Math Server Testleri

| Test | Kontrol Edilen | Beklenen Sonuç |
|------|----------------|----------------|
| Connection | Sunucu bağlantısı | Session oluşturulmalı |
| Addition | 15 + 27 | "42" içermeli |
| Multiplication | 8 × 12 | "96" içermeli |
| Invalid | Geçersiz kaynak | Exception fırlatmalı |
| Both Resources | Her iki kaynak | Sıralı çalışmalı |

## 🛠️ Geliştirme

### Yeni Bir Kaynak Ekleme

```python
@mcp.resource("resource://yeni-kaynak")
def yeni_kaynak() -> str:
    return "Yeni kaynak yanıtı"
```

### Yeni Test Ekleme

```python
@pytest.mark.asyncio
async def test_yeni_kaynak():
    """Yeni kaynak testi"""
    # Test kodunuz
    assert response is not None
```

## 📝 Notlar

- Tüm sunucular `stdio` transport protokolü kullanır
- Testler asenkron (`asyncio`) olarak çalışır
- Her test bağımsızdır ve izole edilmiştir
- Hata yönetimi tüm testlerde kontrol edilir

## 🤝 Katkıda Bulunma

1. Yeni özellikler eklerken test yazın
2. Mevcut testlerin başarılı olduğundan emin olun
3. Kod standartlarına uyun
4. README'yi güncelleyin

## 📄 Lisans

Bu proje eğitim amaçlıdır ve özgürce kullanılabilir.

## 🎓 Öğrenme Kaynakları

- [MCP Dokumentasyonu](https://modelcontextprotocol.io)
- [FastMCP Kullanımı](https://github.com/modelcontextprotocol/fastmcp)
- [Pytest Dokümantasyonu](https://docs.pytest.org)

---

**Geliştirici:** MCP Öğrenme Projesi  
**Versiyon:** 1.0.0  
**Son Güncelleme:** 2025

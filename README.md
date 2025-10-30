# 🧩 Penjelasan Kode CRUD Product (Gin + SQL)

## 📦 Struktur Umum
Kode ini berisi **CRUD (Create, Read, Update, Delete)** untuk data **produk** menggunakan framework **Gin** dan database **SQL**.

---

## 🧱 Struct (Model)

```go
type Product struct {
	ID          int64
	Name        string
	Price       float64
	CategoryID  int64
	Category    string
	ImageURL    string
	Images      []string
	Sizes       []SizeOption
	Stock       int
	Description string
}

type SizeOption struct {
	Size  string
	Stock int
}
```

- **`Product`** → representasi satu produk.
- **`SizeOption`** → ukuran dan stok tiap ukuran (misal: S, M, L, XL).

---

## 🟢 1. GetProducts

```go
func GetProducts(c *gin.Context)
```

- Ambil semua produk dari database.  
- Bisa difilter pakai query `?category=nama_kategori`.  
- Join tabel `products` dan `categories`.  
- Parse kolom JSON (`images`, `sizes`) dari string ke array.  
- Return daftar produk dalam bentuk JSON.

**Alur:**
1. Ambil `category` dari query string.  
2. Jalankan query SQL.  
3. Unmarshal data JSON dari database.  
4. Kirim response ke client dalam format JSON.

---

## 🟢 2. GetProductByID

```go
func GetProductByID(c *gin.Context)
```

- Ambil **1 produk** berdasarkan `id`.  
- Jika tidak ditemukan → return `404`.  
- Parse kolom JSON (`images`, `sizes`).  
- Return detail produk dalam JSON.

**Contoh endpoint:**  
```
GET /api/products/3
```

---

## 🟡 3. CreateProduct

```go
func CreateProduct(c *gin.Context)
```

- Terima input via **form-data**:
  - `name`, `price`, `description`, `category_id`, `sizes`, `images`
- Upload gambar ke folder `./images/` dan simpan URL-nya.  
- Hitung **total stok** dari semua ukuran (`sizes`).  
- Simpan produk baru ke tabel `products`.  
- Return produk yang baru dibuat.

**Langkah utama:**
1. Ambil data dari form (`c.PostForm`, `c.MultipartForm`).  
2. Upload gambar dan simpan URL.  
3. Hitung total stok dari field `sizes`.  
4. Simpan data ke database.  
5. Kirim response `201 Created`.

---

## 🟠 4. UpdateProduct

```go
func UpdateProduct(c *gin.Context)
```

- Edit produk berdasarkan `id`.  
- Bisa update semua field seperti `name`, `price`, `sizes`, `images`, dll.  
- Upload gambar baru (kalau ada) dan gabungkan dengan gambar lama (`existingImages`).  
- Update data di database.  
- Return produk yang sudah diperbarui.

**Contoh endpoint:**  
```
PUT /api/products/3
```

---

## 🔴 5. DeleteProduct

```go
func DeleteProduct(c *gin.Context)
```

- Hapus produk berdasarkan `id`.  
- Jika produk tidak ditemukan → `404 Not Found`.  
- Jika berhasil → return pesan `"product deleted"`.

**Contoh endpoint:**  
```
DELETE /api/products/3
```

---

## ⚙️ Ringkasan Fungsi

| Fungsi | Tujuan | HTTP Method |
|--------|---------|-------------|
| `GetProducts` | Ambil semua produk | **GET** |
| `GetProductByID` | Ambil 1 produk | **GET** |
| `CreateProduct` | Tambah produk baru | **POST** |
| `UpdateProduct` | Edit produk | **PUT / PATCH** |
| `DeleteProduct` | Hapus produk | **DELETE** |

---

## 💡 Inti Utama
- Semua endpoint pakai **Gin Context (`c *gin.Context`)**.  
- Gambar diupload ke folder `./images`.  
- Kolom `images` dan `sizes` disimpan dalam bentuk **JSON di database**.  
- Field `stock` dihitung otomatis dari semua ukuran.


You said:

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"time"

	db "github.com/Maxiegame092/pbp-app/DB"
	"github.com/gin-gonic/gin"
)


type Product struct {
	ID          int64           json:"id"
	Name        string          json:"name"
	Price       float64         json:"price"
	CategoryID 	int64			json:"category_id"
	Category    string          json:"category"
	ImageURL    string          json:"imageUrl"
	Images      []string        json:"images"
	Sizes       []SizeOption    json:"sizes"  
	Stock       int             json:"stock"
	Description string          json:"description"
}

type SizeOption struct {
	Size  string json:"size"
	Stock int    json:"stock"
}

func GetProducts(c *gin.Context) {

	category := c.Query("category")

	query := 
    SELECT 
		p.id, p.name, p.price, p.category_id, IFNULL(c.name, '') as category,
		p.image_url, p.images, p.sizes, p.stock, p.description
	FROM products p
	LEFT JOIN categories c ON p.category_id = c.id
	

	args := []any{}
	if category != "" {
		query += " WHERE c.name = ?"
		args = append(args, category)
	}

	rows, err := db.DB.Query(query, args...)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "db query error"})
		return
	}
	defer rows.Close()
	
	var out []Product
	for rows.Next() {
		var p Product
		var imagesJSON, sizesJSON sql.NullString
		if err := rows.Scan(
			&p.ID, &p.Name, &p.Price, &p.CategoryID, &p.Category,
			&p.ImageURL, &imagesJSON, &sizesJSON, &p.Stock, &p.Description,
		); err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "scan error"})
			return
		}
		if imagesJSON.Valid {
			if err := json.Unmarshal([]byte(imagesJSON.String), &p.Images); err != nil {
			}
		}

		if sizesJSON.Valid {
			err := json.Unmarshal([]byte(sizesJSON.String), &p.Sizes)
			if err != nil {
				var temp string
				if err2 := json.Unmarshal([]byte(sizesJSON.String), &temp); err2 == nil {
					_ = json.Unmarshal([]byte(temp), &p.Sizes)
				} else {
					fmt.Println("⚠️ JSON unmarshal sizes error:", err)
				}
			}
		}
				
		out = append(out, p)
	}
	c.JSON(http.StatusOK, out)
}


func GetProductByID(c *gin.Context) {
	idStr := c.Param("id")
	id, err := strconv.ParseInt(idStr, 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid id"})
		return
	}

	var p Product
	var imagesJSON, sizesJSON sql.NullString

	err = db.DB.QueryRow(
		SELECT 
			p.id, p.name, p.price, p.category_id, c.name as category, 
			p.image_url, p.images, p.sizes, p.stock, p.description
		FROM products p
		JOIN categories c ON p.category_id = c.id
		WHERE p.id = ?
	, id).Scan(
		&p.ID, &p.Name, &p.Price, &p.CategoryID, &p.Category,
		&p.ImageURL, &imagesJSON, &sizesJSON, &p.Stock, &p.Description,
	)

	if err == sql.ErrNoRows {
		c.JSON(http.StatusNotFound, gin.H{"error": "not found"})
		return
	} else if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "db error"})
		return
	}

	if imagesJSON.Valid {
		_ = json.Unmarshal([]byte(imagesJSON.String), &p.Images)
	}
	
	if sizesJSON.Valid {
		err := json.Unmarshal([]byte(sizesJSON.String), &p.Sizes)
		if err != nil {
			var temp string
			if err2 := json.Unmarshal([]byte(sizesJSON.String), &temp); err2 == nil {
				_ = json.Unmarshal([]byte(temp), &p.Sizes)
			} else {
				fmt.Println("⚠️ JSON unmarshal sizes error:", err)
			}
		}
	}


	c.JSON(http.StatusOK, p)
}



func CreateProduct(c *gin.Context) {
    name := c.PostForm("name")
    category := c.PostForm("category_id")  
    priceStr := c.PostForm("price")
    description := c.PostForm("description")

    sizesStr := c.PostForm("sizes")
    var sizes []map[string]interface{}
    var totalStock int
    if sizesStr != "" {
        if err := json.Unmarshal([]byte(sizesStr), &sizes); err == nil {
            for _, s := range sizes {
                if stockVal, ok := s["stock"].(float64); ok {
                    totalStock += int(stockVal)
                }
            }
        }
    }

    price, _ := strconv.ParseFloat(priceStr, 64)

    form, _ := c.MultipartForm()
    files := form.File["images"]

    var uploadedPaths []string
    for _, file := range files {
        filename := strconv.FormatInt(time.Now().UnixNano(), 10) + "_" + file.Filename
        savePath := "./images/" + filename
        if err := c.SaveUploadedFile(file, savePath); err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }
        uploadedPaths = append(uploadedPaths, "http://localhost:5000/images/"+filename)
    }

    existingImages := c.PostFormArray("existingImages")
    allImages := append(existingImages, uploadedPaths...)

    imagesJSON, _ := json.Marshal(allImages)
	
	var sizesData []map[string]interface{}
	_ = json.Unmarshal([]byte(sizesStr), &sizesData)
	sizesJSONBytes, _ := json.Marshal(sizesData)
	sizesJSON := string(sizesJSONBytes)


    var categoryID int
    err := db.DB.QueryRow(
        SELECT id FROM categories WHERE id = ? OR name = ? LIMIT 1
    , category, category).Scan(&categoryID)
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "kategori tidak ditemukan"})
        return
    }

    query := 
        INSERT INTO products (name, price, category_id, image_url, images, sizes, stock, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    
    res, err := db.DB.Exec(query,
        name, price, categoryID,
        allImages[0], string(imagesJSON), string(sizesJSON), totalStock, description,
    )

    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }

    id, _ := res.LastInsertId()

    var categoryName string
    _ = db.DB.QueryRow("SELECT name FROM categories WHERE id = ?", categoryID).Scan(&categoryName)

    c.JSON(http.StatusCreated, gin.H{
        "id":          id,
        "name":        name,
        "price":       price,
        "stock":       totalStock,
        "category":    categoryName,
        "description": description,
        "images":      allImages,
        "sizes":       sizes,
    })
}


func UpdateProduct(c *gin.Context) {
    idStr := c.Param("id")
    id, _ := strconv.ParseInt(idStr, 10, 64)

    name := c.PostForm("name")
    category := c.PostForm("category_id")  
    priceStr := c.PostForm("price")
    description := c.PostForm("description")

    price, _ := strconv.ParseFloat(priceStr, 64)

    sizesStr := c.PostForm("sizes")
    var sizes []map[string]interface{}
    var totalStock int
    if sizesStr != "" {
        if err := json.Unmarshal([]byte(sizesStr), &sizes); err == nil {
            for _, s := range sizes {
                if stockVal, ok := s["stock"].(float64); ok {
                    totalStock += int(stockVal)
                }
            }
        }
    }

    form, _ := c.MultipartForm()
    files := form.File["images"]

    var uploadedPaths []string
    for _, file := range files {
        filename := strconv.FormatInt(time.Now().UnixNano(), 10) + "_" + file.Filename
        savePath := "./images/" + filename
        if err := c.SaveUploadedFile(file, savePath); err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }
        uploadedPaths = append(uploadedPaths, "http://localhost:5000/images/"+filename)
    }

    existingImages := c.PostFormArray("existingImages")
    allImages := append(existingImages, uploadedPaths...)

	imagesJSON, _ := json.Marshal(allImages)

	var sizesData []map[string]interface{}
	_ = json.Unmarshal([]byte(sizesStr), &sizesData)
	sizesJSONBytes, _ := json.Marshal(sizesData)
	sizesJSON := string(sizesJSONBytes)


    var categoryID int
    err := db.DB.QueryRow(
        SELECT id FROM categories WHERE id = ? OR name = ? LIMIT 1
    , category, category).Scan(&categoryID)
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "kategori tidak ditemukan"})
        return
    }

    query := 
        UPDATE products
        SET name = ?, price = ?, category_id = ?, image_url = ?, images = ?, sizes = ?, stock = ?, description = ?
        WHERE id = ?
    
    _, err = db.DB.Exec(query,
        name, price, categoryID, allImages[0], string(imagesJSON), string(sizesJSON), totalStock, description, id,
    )
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }

	var categoryName string
	_ = db.DB.QueryRow("SELECT name FROM categories WHERE id = ?", categoryID).Scan(&categoryName)

	c.JSON(http.StatusOK, gin.H{
		"id":          id,
		"name":        name,
		"price":       price,
		"stock":       totalStock,
		"category":    categoryName,
		"description": description,
		"images":      allImages,
		"sizes":       sizes,
	})

}



func DeleteProduct(c *gin.Context) {
	idStr := c.Param("id")
	id, err := strconv.ParseInt(idStr, 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid id"})
		return
	}

	res, err := db.DB.Exec("DELETE FROM products WHERE id = ?", id)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "db error", "detail": err.Error()})
		return
	}

	rowsAffected, _ := res.RowsAffected()
	if rowsAffected == 0 {
		c.JSON(http.StatusNotFound, gin.H{"error": "product not found"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "product deleted"})
} 

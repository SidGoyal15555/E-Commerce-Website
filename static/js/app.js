const productGrid = document.getElementById("productGrid");
const searchInput = document.getElementById("searchInput");
const categoryFilter = document.getElementById("categoryFilter");
const statusMessage = document.getElementById("statusMessage");

function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (character) => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;"
    })[character]);
}

function renderProducts(products) {
    productGrid.innerHTML = "";

    if (products.length === 0) {
        statusMessage.textContent = "No products match your search.";
        return;
    }

    statusMessage.textContent = `${products.length} product(s) found.`;

    for (const product of products) {
        const card = document.createElement("article");
        card.className = "product-card";

        card.innerHTML = `
            <img src="${escapeHtml(product.image_url)}"
                 alt="${escapeHtml(product.name)}"
                 onerror="this.src='https://placehold.co/600x400?text=Product'">
            <div class="card-content">
                <span class="category">${escapeHtml(product.category)}</span>
                <h3>${escapeHtml(product.name)}</h3>
                <p>${escapeHtml(product.description)}</p>
                <div class="card-footer">
                    <strong>₹${Number(product.price).toFixed(2)}</strong>
                    <a class="details-link" href="/products/${product.id}">
                        View details
                    </a>
                </div>
            </div>
        `;

        productGrid.appendChild(card);
    }
}

async function loadProducts() {
    const params = new URLSearchParams();
    const query = searchInput.value.trim();
    const category = categoryFilter.value;

    if (query) params.set("q", query);
    if (category) params.set("category", category);

    statusMessage.textContent = "Loading products...";

    try {
        const response = await fetch(`/api/products?${params.toString()}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Could not load products.");
        }

        renderProducts(data.products);
    } catch (error) {
        productGrid.innerHTML = "";
        statusMessage.textContent = error.message;
    }
}

async function loadCategories() {
    try {
        const response = await fetch("/api/categories");
        if (!response.ok) {
            throw new Error("Could not load categories.");
        }

        const categories = await response.json();

        for (const category of categories) {
            const option = document.createElement("option");
            option.value = category;
            option.textContent = category;
            categoryFilter.appendChild(option);
        }
    } catch (error) {
        statusMessage.textContent = error.message;
    }
}

searchInput.addEventListener("input", loadProducts);
categoryFilter.addEventListener("change", loadProducts);

async function initializePage() {
    await loadCategories();
    await loadProducts();
}

initializePage();

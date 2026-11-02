const detailsContainer = document.getElementById("productDetails");
const statusElement = document.getElementById("statusMessage");

function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (character) => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;"
    })[character]);
}

async function loadProductDetails() {
    try {
        const response = await fetch(`/api/products/${PRODUCT_ID}`);
        const product = await response.json();

        if (!response.ok) {
            throw new Error(product.error || "Product could not be loaded.");
        }

        statusElement.textContent = "";

        detailsContainer.innerHTML = `
            <article class="detail-card">
                <div class="detail-image-wrap">
                    <img src="${escapeHtml(product.image_url)}"
                         alt="${escapeHtml(product.name)}"
                         onerror="this.src='https://placehold.co/800x600?text=Product'">
                </div>
                <div class="detail-content">
                    <span class="category">${escapeHtml(product.category)}</span>
                    <h1>${escapeHtml(product.name)}</h1>
                    <p>${escapeHtml(product.description)}</p>
                    <h2>₹${Number(product.price).toFixed(2)}</h2>
                    <p class="product-id">Product ID: ${product.id}</p>
                </div>
            </article>
        `;
    } catch (error) {
        statusElement.textContent = error.message;
    }
}

loadProductDetails();

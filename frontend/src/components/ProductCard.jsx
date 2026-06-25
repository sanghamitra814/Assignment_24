function ProductCard({ product }) {
  return (
    <div className="card">
      <img src={product.image} alt={product.name} />

      <div className="card-content">
        <h2>{product.name}</h2>

        <p className="price">₹{product.price}</p>

        <span className="category">
          {product.category}
        </span>

        <p>{product.description}</p>

        <p className="stock">
          Stock Available: {product.stock}
        </p>

        <button className="buy-btn">
          Add To Cart
        </button>
      </div>
    </div>
  );
}

export default ProductCard;
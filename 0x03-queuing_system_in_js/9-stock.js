import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Redis client setup
const client = redis.createClient();
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// Data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Helper Functions
const getItemById = (id) => listProducts.find((item) => item.itemId === id);

const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
};

// Routes
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    product.initialAvailableQuantity - (reservedStock || 0);

  res.json({
    ...product,
    currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    product.initialAvailableQuantity - (reservedStock || 0);

  if (currentQuantity <= 0) {
    res.status(400).json({
      status: 'Not enough stock available',
      itemId,
    });
    return;
  }

  await reserveStockById(itemId, (reservedStock || 0) + 1);

  res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

// Start server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

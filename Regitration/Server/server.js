const express    = require('express');
const mongoose   = require('mongoose');
const cors       = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Connect with hardcoded URL
mongoose.connect('mongodb://localhost:27017/RuVMultitoolv1', {
  useNewUrlParser:    true,
  useUnifiedTopology: true
});

const userSchema = new mongoose.Schema({
  userId:   String,
  password: String
});

const User = mongoose.model('Auth', userSchema, 'Auth');

app.post('/signup', async (req, res) => {
  const { userId, password } = req.body;
  if (!userId || !password) {
    return res.status(400).send('Missing fields');
  }

  try {
    if (await User.findOne({ userId })) {
      return res.status(409).send('User already exists');
    }
    await new User({ userId, password }).save();
    res.status(201).send('User created');
  } catch {
    res.status(500).send('Server error');
  }
});

app.listen(3000, () => {
  console.log('✅ Server running on port 3000');
});
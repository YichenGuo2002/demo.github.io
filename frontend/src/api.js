// Basic JS (or React useEffect)
import axios from 'axios';

// get Starter data
export default async function api(){
  const response = await axios.get('http://localhost:5000/api/data');
  return response.data;
};
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BingoList from './components/BingoList';
import BingoElementForm from './components/BingoElementForm';

const apiUrl = 'http://localhost:5000/api/bingo';

function App() {
  const [bingoElements, setBingoElements] = useState([]);
  const [editingElement, setEditingElement] = useState(null);

  useEffect(() => {
    fetchBingoElements();
  }, []);

  const fetchBingoElements = async () => {
    try {
      const response = await axios.get(apiUrl);
      setBingoElements(response.data);
    } catch (error) {
      console.error("Error fetching bingo elements:", error);
    }
  };

  const updateBingoElement = async (id, updatedElement) => {
    try {
      await axios.put(`${apiUrl}/${id}`, updatedElement);
      fetchBingoElements();
    } catch (error) {
      console.error("Error updating bingo element:", error);
    }
  };

  const deleteBingoElement = async (id) => {
    try {
      await axios.delete(`${apiUrl}/${id}`);
      fetchBingoElements();
    } catch (error) {
      console.error("Error deleting bingo element:", error);
    }
  };

  return (
    <div>
      <h1>Bingo Admin Panel</h1>
      {}
      {editingElement && (
        <BingoElementForm
          onSubmit={updateBingoElement}
          editingElement={editingElement}
          setEditingElement={setEditingElement}
        />
      )}
      <BingoList
        bingoElements={bingoElements}
        onDelete={deleteBingoElement}
        onEdit={setEditingElement}
      />
    </div>
  );
}

export default App;

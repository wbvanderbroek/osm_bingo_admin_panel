import React, { useState, useEffect } from 'react';

function BingoElementForm({ onSubmit, editingElement, setEditingElement }) {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');

  useEffect(() => {
    if (editingElement) {
      setName(editingElement.name);
      setDescription(editingElement.description);
      setLatitude(editingElement.latitude);
      setLongitude(editingElement.longitude);
    }
  }, [editingElement]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const element = { name, description, latitude: parseFloat(latitude), longitude: parseFloat(longitude) };
    onSubmit(editingElement.id, element); 
    clearForm();
  };

  const clearForm = () => {
    setName('');
    setDescription('');
    setLatitude('');
    setLongitude('');
    setEditingElement(null);
  };

  return (
    <div>
      <h2>Edit Bingo Element</h2> {}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Latitude"
          value={latitude}
          onChange={(e) => setLatitude(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Longitude"
          value={longitude}
          onChange={(e) => setLongitude(e.target.value)}
          required
        />
        <button type="submit">Update Element</button> {}
        {editingElement && <button onClick={clearForm}>Cancel</button>}
      </form>
    </div>
  );
}

export default BingoElementForm;

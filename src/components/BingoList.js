import React from 'react';

function BingoList({ bingoElements, onEdit }) {
  return (
    <ul>
      {bingoElements.map((element) => (
        <li key={element.id}>
          <h3>{element.name}</h3>
          <p>{element.description}</p>
          <button onClick={() => onEdit(element)}>Edit</button>
        </li>
      ))}
    </ul>
  );
}

export default BingoList;

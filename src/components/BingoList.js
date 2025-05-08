import React from 'react';

function BingoList({ bingoElements, onDelete, onEdit }) {
  return (
    <div>
      <h2>Bingo Elements</h2>
      <ul>
        {bingoElements.map((element) => (
          <li key={element.id}>
            <span>{element.name} - {element.description}</span>
            <button onClick={() => onEdit(element)}>Edit</button>
            <button onClick={() => onDelete(element.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BingoList;

import React, { useState } from "react";
import AddNoteModal from "../components/AddNoteModal";

const NotesPanel = ({ projectId, userId, notes, onAddNote }) => {
  const [showModal, setShowModal] = useState(true);

  return (
    <div className="notes-section">
        
      <div className="notes-header">
        <h2>Notes</h2>
        <button onClick={() => setShowModal(true)}>+ Add Note</button>
      </div>

      <ul className="notes-list">
        {notes.map((note) => (
          <li key={note.id}>{note.content}</li>
        ))}
      </ul>

      {showModal && (
        <AddNoteModal
          projectId={projectId}
          userId={userId}
          onClose={() => setShowModal(false)}
          onSave={(data) => {
            onAddNote(data);
            // setShowModal(false);
          }}
        />
      )}
    </div>
  );
};

export default NotesPanel;

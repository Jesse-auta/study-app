import React, { useState } from "react";
import AddNoteModal from "../components/AddNoteModal";
import { ChevronUp, ChevronDown } from "lucide-react"

const NotesPanel = ({ projectId, userId, notes, onAddNote }) => {
  const [showModal, setShowModal] = useState(true);
  const [showNotes, setShowNotes] = useState(false);

  return (
    <div className="notes-section">
        
        <div className="notes-header">
            <h2>Notes</h2>
            <div >
                <button className="add-button" onClick={() => setShowNotes(!showNotes)}>
                    {showNotes? <ChevronUp size={18}/>: <ChevronDown size={18}/>}
                </button>
                {/* <button className="add-button" onClick={() => setShowModal(true)}>+ Add Note</button> */}

            </div>
        </div>
        {showNotes && (
            <div className="notes">
                {notes.length > 0 ? (
                    <ul className="notes-list">
                        {notes.map((note) => (
                            <li key={note.id}>{note.content}</li>
                        ))}
                    </ul>
                ): (<p>No Notes Yet</p>)}
            </div>
        )}
      
      {/* <hr /> */}

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

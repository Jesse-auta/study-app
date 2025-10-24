import React, { useState } from "react";

const AddNoteModal = ({ projectId, userId, onClose, onSave }) => {
  const [content, setContent] = useState("");

  const handleSubmit = () => {
    if (content.trim()) {
      onSave({ content, project_id: projectId, user_id: userId });
      setContent("");
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        
        <div className="modal-actions">
            <h3>Add Note</h3>
            <button onClick={handleSubmit}>✔</button>
            {/* <button onClick={onClose}>Cancel</button> */}
        </div>
        <textarea className="note-modal"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Write your note here..."
        />
        
      </div>
    </div>
  );
};

export default AddNoteModal;

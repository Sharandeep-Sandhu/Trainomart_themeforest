"use client";

import React, { useState } from "react";
import { FaCommentDots } from "react-icons/fa"; // Import feedback icon

const FeedbackButton = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);

    const openModal = () => setIsModalOpen(true);
    const closeModal = () => setIsModalOpen(false);

    return (
        <div>
            {/* Sidebar Button */}
            <button
                onClick={openModal}
                className="fixed right-0 top-1/2 transform -translate-y-1/2 bg-blue-500 text-white p-3 rounded-l-lg shadow-lg flex items-center hover:bg-blue-700 transition duration-300 z-50"
            >
                <FaCommentDots className="mr-2" />
                Feedback
            </button>

            {/* Modal */}
            {isModalOpen && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
                    <div className="bg-white p-6 rounded-lg w-96">
                        <h2 className="text-xl font-bold mb-4">Feedback</h2>
                        <textarea
                            className="w-full p-2 border border-gray-300 rounded-lg mb-4"
                            placeholder="Enter your feedback..."
                            rows="4"
                        ></textarea>
                        <div className="flex justify-end space-x-2">
                            <button
                                onClick={closeModal}
                                className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400 transition duration-300"
                            >
                                Close
                            </button>
                            <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition duration-300">
                                Submit
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default FeedbackButton;

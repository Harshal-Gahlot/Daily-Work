export default function InputBtn({ onClick, type, placeholder }) {
    return <span onClick={onClick} 
    className="rounded-md max-w-72 text-xl cursor-pointer py-3 bg-blue-400 px-4">
        <input type={type} placeholder={placeholder} className="bg-blue-400 placeholder:text-gray-600 outline-none" />
    </span>;
}
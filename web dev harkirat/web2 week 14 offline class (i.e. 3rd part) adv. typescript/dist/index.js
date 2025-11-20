"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const users = new Map();
users.set("res", 4);
users.set("pec", 5);
const user = users.get("res");
console.log('user', user);
// type User = {
//     age: number;
//     name: string;
// };
// // not great/clear way
// // type Users = {
// //     [id: string]: User;
// // };
// // better/clear way to do:
// type Users = Record<string, User>
// const users: Users = {
//     "123": {age: 12, name: "123"},
//     "321": {age: 13, name: "abc"}
// }
// console.log('users', users)
//# sourceMappingURL=index.js.map
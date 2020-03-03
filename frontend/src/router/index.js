import Vue from 'vue';
import VueRouter from 'vue-router';
import ReverseString from '@/components/ReverseString'
import FileUpload from '@/components/FileUpload'

Vue.use(VueRouter);

const routes = [
  {
    path: '/reverse',
    name: 'ReverseString',
    component: ReverseString,
  },
  {
    path: '/files',
    name: 'FileUpload',
    component: FileUpload,
  }
];

const router = new VueRouter({
  routes,
});

export default router;

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  try {
    const [signUpResult, uploadPhotoResult] = await Promise.all([
      signUpUser(firstName, lastName),
      uploadPhoto(fileName),
    ]);

    return [
      { status: 'fulfilled', value: signUpResult },
      { status: 'fulfilled', value: uploadPhotoResult },
    ];
  } catch (error) {
    const errorMessage = `Error: ${error.message}`;
    return [
      { status: 'rejected', value: errorMessage },
      { status: 'rejected', value: errorMessage },
    ];
  }
}

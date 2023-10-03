import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {

  try {
    const signUpResult = await signUpUser(firstName, lastName);
    const uploadPhotoResult = await uploadPhoto(fileName);

    return [
      { status: 'fulfilled', value: signUpResult },
      { status: 'fulfilled', value: uploadPhotoResult },
    ];
  } catch (error) {
    return [
      { status: 'rejected', value: `Error: ${error.message}` },
      { status: 'rejected', value: 'Photo upload failed' },
    ];
  }
}
